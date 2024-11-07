# Definir colores
GREEN='%F{green}'
CYAN='%F{cyan}'
MAGENTA='%F{magenta}'
RESET='%f'

# Personalizar prompt
PROMPT='${GREEN}%n${RESET} - ${CYAN}[%~]${RESET}${MAGENTA}(%1v)${RESET}:~$ '

# Opciones adicionales para el directorio y rama actual
autoload -Uz vcs_info
zstyle ':vcs_info:*' enable git
precmd() { vcs_info }
setopt prompt_subst
PROMPT='${GREEN}%n${RESET} - ${CYAN}[%~]${RESET}${MAGENTA}(${vcs_info_msg_0_})${RESET}:~$ '

