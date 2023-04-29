## Description

OpenVoiceOS STT plugin for [FunASR](https://github.com/alibaba-damo-academy/FunASR)


## Install

`pip install ovos-stt-plugin-funasr`

## Configuration

models here https://alibaba-damo-academy.github.io/FunASR/en/modelscope_models.html

- `damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch`
- `damo/speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1`
- `damo/speech_UniASR_asr_2pass-zh-cn-16k-common-vocab8358-tensorflow1-online`
- `damo/speech_UniASR-large_asr_2pass-zh-cn-16k-common-vocab8358-tensorflow1-offline`

```json
  "stt": {
    "module": "ovos-stt-plugin-funasr",
    "ovos-stt-plugin-funasr": {
        "model": "damo/speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1"
    }
  }
 
```

## Models

Models will be auto downloaded by faster whisper on plugin load

