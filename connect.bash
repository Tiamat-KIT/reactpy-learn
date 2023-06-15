#!/bin/bash
#This is KIT proxy connect script.
#You can use "proxyon" alias.
#"echo "alias proxyon='source ~/.proxy.sh' >> .bashrc"
#Usage: sh .proxy.sh or alias "proxyon"
#(Tatsuya Imai, Japan)

export http_proxy="http://wwwproxy.kanazawa-it.ac.jp:8080/"
export https_proxy="http://wwwproxy.kanazawa-it.ac.jp:8080/"
# git settings
git config --global http.proxy http://wwwproxy.kanazawa-it.ac.jp:8080
# npm settings
npm -g config set http-proxy "http://wwwproxy.kanazawa-it.ac.jp:8080/"
npm -g config set https-proxy "http://wwwproxy.kanazawa-it.ac.jp:8080/"
npm -g config set registry "http://registry.npmjs.org/"
# yarn settings
yarn config set proxy http://wwwproxy.kanazawa-it.ac.jp:8080
yarn config set https-proxy http://wwwproxy.kanazawa-it.ac.jp:8080
echo "Set proxy"