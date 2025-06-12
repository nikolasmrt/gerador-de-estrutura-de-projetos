import os
import sys
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml

# Utilities
def setup_logger():
    """Configura um logger simples para feedback ao usuário."""
    import logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger()

def create_directory(path):
    """Cria um diretório se ele não existir."""
    try:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Diretório criado: {path}")
    except OSError as e:
        logger.error(f"Erro ao criar diretório {path}: {e}")
        sys.exit(1)

def render_and_save_template(env, template_path, output_path, context):
    
    try:
       
        final_output_path = output_path.replace('', '')

        template = env.get_template(template_path)
        output_content = template.render(context)

        with open(final_output_path, 'w', encoding='utf-8') as f:
            f.write(output_content)
        logger.info(f"Arquivo gerado: {final_output_path}")
    except Exception as e:
        logger.error(f"Erro ao renderizar/salvar template '{template_path}' para '{output_path}': {e}")
        sys.exit(1)

# Main 
def generate_project(project_type: str, output_root_dir: str, custom_vars: dict = None):
   
    if custom_vars is None:
        custom_vars = {}

    logger.info(f"Iniciando a geração do projeto do tipo '{project_type}' em '{output_root_dir}'...")

    # Carregar configurações de projetos
    try:
        with open('config/projects.yaml', 'r', encoding='utf-8') as f:
            projects_config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error("Arquivo de configuração 'config/projects.yaml' não encontrado. Certifique-se de que ele existe.")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Erro ao carregar o arquivo 'config/projects.yaml': {e}")
        sys.exit(1)

    project_info = projects_config.get(project_type)
    if not project_info:
        logger.error(f"Tipo de projeto '{project_type}' não encontrado nas configurações.")
        logger.info(f"Tipos disponíveis: {', '.join(projects_config.keys())}")
        sys.exit(1)

    template_dir = os.path.join('templates', project_info['template_dir'])
    if not os.path.isdir(template_dir):
        logger.error(f"Diretório de templates '{template_dir}' para o tipo de projeto '{project_type}' não encontrado.")
        sys.exit(1)

    # Coletar variáveis
    context = project_info.get('variables', {})
    context.update(custom_vars) # Sobrescreve com variáveis personalizadas

    # Se houver variáveis customizadas passadas pela linha de comando, elas sobrescrevem as do projeto
    for key, value in context.items():
        if value is None or value == "":
            user_input = input(f"Por favor, insira o valor para '{key}' (padrão: {value if value else 'Nenhum'}): ")
            context[key] = user_input if user_input else value

    
    for key, value in context.items():
        if value is None or value == "":
            logger.error(f"Variável '{key}' é obrigatória e não foi fornecida.")
            sys.exit(1)

    
    
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml', 'j2'])
    )

    
    create_directory(output_root_dir)

    
    for root, dirs, files in os.walk(template_dir):
        
        
        relative_path = os.path.relpath(root, template_dir)
        
   
        output_dir = os.path.join(output_root_dir, relative_path)

        # Crie diretórios no destino (incluindo subdiretórios de templates)
        create_directory(output_dir)

        for file in files:
            
            template_internal_path = os.path.join(relative_path, file)

            
            output_file_path = os.path.join(output_dir, file)

            if file.endswith('.j2'):
               
                render_and_save_template(env, template_internal_path, output_file_path, context)
            else:
                # Copiar arquivos estáticos diretamente
                try:
                    shutil.copy2(os.path.join(root, file), output_file_path)
                    logger.info(f"Arquivo copiado: {output_file_path}")
                except IOError as e:
                    logger.error(f"Erro ao copiar arquivo {os.path.join(root, file)} para {output_file_path}: {e}")
                    sys.exit(1)

    logger.info(f"\n[+] Projeto '{context.get('project_name', project_type)}' gerado com sucesso em '{output_root_dir}'!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        logger.info("Uso: python main.py <tipo_do_projeto> <diretorio_destino> [OPÇÕES]")
        logger.info("Exemplo: python main.py nodejs-express meu-app-node")
        logger.info("Opções: --var key=value (para passar variáveis customizadas)")
        sys.exit(1)

    project_type = sys.argv[1]
    output_directory = sys.argv[2]
    
    # Analisar variáveis customizadas da linha de comando
    cli_vars = {}
    for arg in sys.argv[3:]:
        if arg.startswith('--var='):
            try:
                key_value = arg[len('--var='):].split('=', 1)
                if len(key_value) == 2:
                    cli_vars[key_value[0]] = key_value[1]
                else:
                    logger.warning(f"Formato inválido para --var: {arg}. Use --var=key=value")
            except Exception as e:
                logger.warning(f"Erro ao analisar a variável '{arg}': {e}")


    generate_project(project_type, output_directory, custom_vars=cli_vars)