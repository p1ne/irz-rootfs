isOn () {
    if [ "$1" = "on" ]; then
        echo "1"
    else
        echo "0"
    fi
}

# setValue file key value
setValue () {
    if grep -qF "$2=" "$1"; then
        sed -e "s/^$2=.*$/$2=$3/" -i $1
    else
        echo "$2=$3" >> $1
    fi
}
