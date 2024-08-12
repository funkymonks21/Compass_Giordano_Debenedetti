# É possível reutilizar containers?

É possível sim, embora ao meu ver possa ser considerado má prática dependendo do contexto.

Reutilizei o container da primeira etapa do desafio usando esses comandos:

```console
giordano@DESKTOP-CHR02UN:~/repositorio/Sprint4/Desafio/etapa1$ sudo docker stop carguru_container
giordano@DESKTOP-CHR02UN:~/repositorio/Sprint4/Desafio/etapa1$ sudo docker start carguru_container
```

Dependendo do contexto pode ser melhor trabalhar com containers diferentes, como por exemplo, utilizar containers para diferentes aplicações.
