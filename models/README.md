# Artefactos del motor inteligente

Git conserva únicamente esta documentación y los manifiestos pequeños de `models/manifests/`.

Los pesos base se obtienen del proveedor original. Los adaptadores LoRA, modelos fusionados y checkpoints se guardan temporalmente en `models/local/` o `checkpoints/`, ambos ignorados por Git. La copia canónica debe publicarse en un bucket S3 con versionado, cifrado y acceso privado.

Un modelo no realiza peticiones por sí mismo. La inferencia requiere: modelo base + adaptador + tokenizer/configuración + código que los cargue (por ejemplo, una API o el motor AulaTeX).
