from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from ovos_plugin_manager.templates.stt import STT
from ovos_plugin_manager.templates.transformers import AudioTransformer
from ovos_utils.log import LOG
from speech_recognition import AudioData


class FunASRSTT(STT):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
        # damo/speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1
        # damo/speech_UniASR_asr_2pass-zh-cn-16k-common-vocab8358-tensorflow1-online
        # damo/speech_UniASR-large_asr_2pass-zh-cn-16k-common-vocab8358-tensorflow1-offline
        model = self.config.get("model") or 'damo/speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1'
        self.inference_pipeline = pipeline(
            task=Tasks.auto_speech_recognition,
            model=model,
        )

    def execute(self, audio: AudioData, language=None):
        rec_result = self.inference_pipeline(
            audio_in=audio.frame_data)
        return rec_result["text"]

    @property
    def available_languages(self) -> set:
        return {"en", "zh-cn"}


if __name__ == "__main__":
    b = FunASRSTT()
    from speech_recognition import Recognizer, AudioFile

    jfk = "/home/miro/PycharmProjects/ovos-stt-plugin-funasr/jfk.wav"
    with AudioFile(jfk) as source:
        audio = Recognizer().record(source)

    a = b.execute(audio, language="en")
    # 2023-04-29 17:42:30.769 - OVOS - __main__:execute:145 - INFO - Detected speech language 'en' with probability 1
    print(a)
    # And so, my fellow Americans, ask not what your country can do for you. Ask what you can do for your country.
