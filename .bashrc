# ~/.bashrc
image_path=$(find "$HOME/.config/neofetch/album_covers" -type f -print0 | shuf -z -n1 | xargs -0)
neofetch --kitty $image_path --size 200px

# [[ $- != *i* ]] && return


alias ls='ls --color=auto -a'
alias grep='grep --color=auto'
alias ye="yay"
alias clear="clear && neofetch --kitty $image_path --size 200px"
alias cls="clear"

alias update="XDG_MENU_PREFIX=arch- kbuildsycoca6"

export QT_QPA_PLATFORMTHEME="qt5ct"
export XDG_MENU_PREFIX="arch- kbuildsycoca6"

eval "$(starship init bash)"

#PS1='[\u@\h \W]\$ '
