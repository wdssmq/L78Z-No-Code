#!/bin/bash
# git-local-backup.sh
# 用于备份本地修改、同步远程、还原本地修改
# 用法：git-local-backup.sh --backup|--reset|--pull|--restore

set -e

WORKDIR=$(pwd)
BACKUP_DIR=~/bak/git-local-backup-$(basename "$WORKDIR")

function backup() {
    mkdir -p "$BACKUP_DIR"
    git diff --name-only | xargs -I{} cp --parents {} "$BACKUP_DIR/" 2>/dev/null || true
    echo "已备份到 $BACKUP_DIR"
}

function reset() {
    git reset --hard
    echo "本地更改已重置"
}

function pull() {
    git pull
    echo "已拉取远程仓库"
}

function restore() {
    if [ -d "$BACKUP_DIR" ]; then
        cp -r "$BACKUP_DIR"/* "$WORKDIR"/
        echo "已还原备份文件"
    else
        echo "未找到备份目录 $BACKUP_DIR"
        exit 1
    fi
}

case "$1" in
    --backup)
        backup
        ;;
    --reset)
        reset
        ;;
    --pull)
        pull
        ;;
    --restore)
        restore
        ;;
    *)
        echo "用法: $0 --backup|--reset|--pull|--restore"
        exit 1
        ;;
esac