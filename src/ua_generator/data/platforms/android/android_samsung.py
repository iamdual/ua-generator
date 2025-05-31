"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import List

from ...filterer import Filterer
from ...version import Version, AndroidVersion
from ....options import Options

# https://en.wikipedia.org/wiki/Android_version_history
# https://source.android.com/setup/start/build-numbers
versions: List[AndroidVersion] = [
    AndroidVersion(Version(major=8, minor=0, build=0), build_numbers=('OPR6.{d}.{v}', 'OPR5.{d}.{v}', 'OPR4.{d}.{v}', 'OPR3.{d}.{v}', 'OPR2.{d}.{v}', 'OPR1.{d}.{v}', 'OPD3.{d}.{v}', 'OPD2.{d}.{v}', 'OPD1.{d}.{v}')),
    AndroidVersion(Version(major=8, minor=1, build=0), build_numbers=('OPM8.{d}.{v}', 'OPM7.{d}.{v}', 'OPM6.{d}.{v}', 'OPM5.{d}.{v}', 'OPM4.{d}.{v}', 'OPM3.{d}.{v}', 'OPM2.{d}.{v}')),
    AndroidVersion(Version(major=9, minor=0, build=0), build_numbers=('PQ3B.{d}.{v}', 'PQ3A.{d}.{v}', 'PQ2A.{d}.{v}', 'PQ1A.{d}.{v}', 'PPR2.{d}.{v}', 'PPR1.{d}.{v}')),
    AndroidVersion(Version(major=10, minor=0, build=0), build_numbers=('QD4A.{d}.{v}', 'QQ3A.{d}.{v}', 'QQ2A.{d}.{v}', 'QQ1D.{d}.{v}', 'QQ1C.{d}.{v}', 'QQ1B.{d}.{v}', 'QQ1A.{d}.{v}', 'QP1A.{d}.{v}', 'QD1A.{d}.{v}')),
    AndroidVersion(Version(major=11, minor=0, build=0), build_numbers=('RD2A.{d}.{v}', 'RQ3A.{d}.{v}', 'RQ2A.{d}.{v}', 'RQ1D.{d}.{v}', 'RQ1C.{d}.{v}', 'RQ1A.{d}.{v}', 'RD1B.{d}.{v}', 'RD1A.{d}.{v}', 'RP1A.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=0, build=0), build_numbers=('SP1A.{d}.{v}', 'SQ1D.{d}.{v}', 'SD1A.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=1, build=0), build_numbers=('SP2A.{d}.{v}', 'SD2A.{d}.{v}', 'SQ3A.{d}.{v}')),
    AndroidVersion(Version(major=13, minor=0, build=0), build_numbers=('TQ3A.{d}.{v}', 'TQ3C.{d}.{v}', 'TQ2B.{d}.{v}', 'TD4A.{d}.{v}', 'TQ2A.{d}.{v}', 'TQ1A.{d}.{v}', 'TD1A.{d}.{v}', 'TP1A.{d}.{v}')),
    AndroidVersion(Version(major=14, minor=0, build=0), build_numbers=('AP2A.{d}.{v}', 'AD1A.{d}.{v}', 'UD2A.{d}.{v}', 'UQ1A.{d}.{v}', 'UP1A.{d}.{v}', 'UD1A.{d}.{v}')),
    AndroidVersion(Version(major=15, minor=0, build=0), build_numbers=('AP4A.{d}.{v}', 'AP3A.{d}.{v}')),
]

# https://firmware.gem-flash.com/index.php?a=downloads&b=folder&id=980
# https://gist.github.com/iamdual/4f7c5a6d9ac1e0de8272fb062cf2aaad
platform_models = ('SM-G390Y', 'SM-G390Y', 'SM-G525F', 'SM-G9006W', 'SM-G9209K', 'SM-316U',
    'SM-318ML', 'SM-318MZ', 'SM-318MZ', 'SM-360GY', 'SM-G110B', 'SM-G110H',
    'SM-G110M', 'SM-G130BT', 'SM-G130BU', 'SM-G130E', 'SM-G130H', 'SM-G130HN',
    'SM-G130M', 'SM-G130U', 'SM-G150N0', 'SM-G150NK', 'SM-G150NL', 'SM-G150NS',
    'SM-G155S', 'SM-G1600', 'SM-G1600', 'SM-G160N', 'SM-G1650', 'SM-G165N',
    'SM-G30HN', 'SM-G310H', 'SM-G310HN', 'SM-G310R', 'SM-G310R5', 'SM-G3139',
    'SM-G3139D', 'SM-G313F', 'SM-G313H', 'SM-G313HN', 'SM-G313HU', 'SM-G313HY',
    'SM-G313HZ', 'SM-G313M', 'SM-G313ML', 'SM-G313MU', 'SM-G313MY', 'SM-G313U',
    'SM-G316F', 'SM-G316HU', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G318',
    'SM-G318H', 'SM-G318HZ', 'SM-G318M', 'SM-G318ML', 'SM-G318MZ', 'SM-G350',
    'SM-G3502', 'SM-G3502C', 'SM-G3502I', 'SM-G3502L', 'SM-G3502T', 'SM-G3502U',
    'SM-G3508', 'SM-G3508I', 'SM-G3508J', 'SM-G3509', 'SM-G3509I', 'SM-G350E',
    'SM-G350L', 'SM-G350M', 'SM-G350X', 'SM-G3518', 'SM-G3556D', 'SM-G3558',
    'SM-G3559', 'SM-G355H', 'SM-G355HN', 'SM-G355HQ', 'SM-G355M', 'SM-G3568V',
    'SM-G357', 'SM-G357FZ', 'SM-G357FZ', 'SM-G357M', 'SM-G3586V', 'SM-G3588V',
    'SM-G3589W', 'SM-G3606', 'SM-G3608', 'SM-G3609', 'SM-G360AZ', 'SM-G360BT',
    'SM-G360F', 'SM-G360F', 'SM-G360FY', 'SM-G360G', 'SM-G360GY', 'SM-G360H',
    'SM-G360HU', 'SM-G360M', 'SM-G360P', 'SM-G360T', 'SM-G360V', 'SM-G361F',
    'SM-G361H', 'SM-G361HU', 'SM-G368T', 'SM-G3812', 'SM-G3812B', 'SM-G3815',
    'SM-G3818', 'SM-G3818ZM', 'SM-G3819D', 'SM-G3858', 'SM-G386F', 'SM-G386T',
    'SM-G386T1', 'SM-G386U', 'SM-G386W', 'SM-G388F', 'SM-G389F', 'SM-G390F',
    'SM-G390W', 'SM-G390Y', 'SM-G398FN', 'SM-G5108', 'SM-G5108Q', 'SM-G5109',
    'SM-G525N', 'SM-G525X', 'SM-G5306W', 'SM-G5308W', 'SM-G5309W', 'SM-G530A',
    'SM-G530AZ', 'SM-G530BT', 'SM-G530F', 'SM-G530FQ', 'SM-G530FZ', 'SM-G530H',
    'SM-G530M', 'SM-G530MU', 'SM-G530P', 'SM-G530R4', 'SM-G530R7', 'SM-G530T',
    'SM-G530T1', 'SM-G530W', 'SM-G530Y', 'SM-G530YZ', 'SM-G531BT', 'SM-G531F',
    'SM-G531H', 'SM-G531M', 'SM-G531Y', 'SM-G532F', 'SM-G532G', 'SM-G532M',
    'SM-G532MT', 'SM-G5500', 'SM-G550FY', 'SM-G550T', 'SM-G550T1', 'SM-G550T2',
    'SM-G5510', 'SM-G5520', 'SM-G5528', 'SM-G570', 'SM-G5700', 'SM-G570F',
    'SM-G570M', 'SM-G570Y', 'SM-G6000', 'SM-G600F', 'SM-G600F', 'SM-G600FY',
    'SM-G600S', 'SM-G6100', 'SM-G610F', 'SM-G610FD', 'SM-G610K', 'SM-G610L',
    'SM-G610M', 'SM-G610S', 'SM-G610Y', 'SM-G611F', 'SM-G611FF', 'SM-G611FFDD',
    'SM-G611K', 'SM-G611L', 'SM-G611M', 'SM-G611M/DS', 'SM-G611MT', 'SM-G611S',
    'SM-G615F', 'SM-G615FU', 'SM-G6200', 'SM-G710', 'SM-G7102', 'SM-G7102T',
    'SM-G7105', 'SM-G7105H', 'SM-G7105K', 'SM-G7105L', 'SM-G7106', 'SM-G7108',
    'SM-G7108V', 'SM-G7109', 'SM-G710L', 'SM-G710S', 'SM-G710x', 'SM-G715F',
    'SM-G715FN', 'SM-G715U', 'SM-G715U1', 'SM-G715W', 'SM-G715X', 'SM-G7200',
    'SM-G7202', 'SM-G720AX', 'SM-G720N0', 'SM-G730A', 'SM-G730V', 'SM-G730W8',
    'SM-G7508Q', 'SM-G7509', 'SM-G750A', 'SM-G750H', 'SM-G770F', 'SM-G770U1',
    'SM-G780F', 'SM-G780G', 'SM-G780X', 'SM-G7810', 'SM-G781B', 'SM-G781BR',
    'SM-G781N', 'SM-G781U', 'SM-G781U1', 'SM-G781V', 'SM-G800A', 'SM-G800F',
    'SM-G800H', 'SM-G800M', 'SM-G800R4', 'SM-G800Y', 'SM-G820A', 'SM-G8508S',
    'SM-G850A', 'SM-G850F', 'SM-G850FQ', 'SM-G850K', 'SM-G850M', 'SM-G850S',
    'SM-G850W', 'SM-G850X', 'SM-G850Y', 'SM-G860P', 'SM-G870A', 'SM-G870D',
    'SM-G870F', 'SM-G870F0', 'SM-G870W', 'SM-G8750', 'SM-G8850', 'SM-G8858',
    'SM-G885F', 'SM-G885K', 'SM-G885L', 'SM-G885S', 'SM-G885X', 'SM-G885Y',
    'SM-G8870', 'SM-G8870', 'SM-G887F', 'SM-G887N', 'SM-G888N0', 'SM-G889A',
    'SM-G889G', 'SM-G890A', 'SM-G891', 'SM-G891A', 'SM-G892A', 'SM-G892A',
    'SM-G892U', 'SM-G9006V', 'SM-G9008V', 'SM-G9009D', 'SM-G900A', 'SM-G900AZ',
    'SM-G900F', 'SM-G900FD', 'SM-G900FQ', 'SM-G900H', 'SM-G900I', 'SM-G900J',
    'SM-G900K', 'SM-G900L', 'SM-G900M', 'SM-G900MD', 'SM-G900P', 'SM-G900R4',
    'SM-G900R6', 'SM-G900R7', 'SM-G900S', 'SM-G900T', 'SM-G900T1', 'SM-G900T3',
    'SM-G900V', 'SM-G900W8', 'SM-G901F', 'SM-G903M', 'SM-G903W', 'SM-G906K',
    'SM-G906L', 'SM-G906S', 'SM-G906SKL', 'SM-G9092', 'SM-G9098', 'SM-G9198',
    'SM-G9200', 'SM-G9208', 'SM-G9209', 'SM-G9209', 'SM-G920A', 'SM-G920AZ',
    'SM-G920F', 'SM-G920FQ', 'SM-G920G1', 'SM-G920I', 'SM-G920K', 'SM-G920L',
    'SM-G920P', 'SM-G920R4', 'SM-G920R6', 'SM-G920R7', 'SM-G920S', 'SM-G920T',
    'SM-G920T1', 'SM-G920V', 'SM-G920W8', 'SM-G920X', 'SM-G925', 'SM-G9250',
    'SM-G925A', 'SM-G925F', 'SM-G925FQ', 'SM-G925I', 'SM-G925ID', 'SM-G925K',
    'SM-G925L', 'SM-G925P', 'SM-G925R4', 'SM-G925R6', 'SM-G925R7', 'SM-G925S',
    'SM-G925T', 'SM-G925V', 'SM-G925W8', 'SM-G925X', 'SM-G925X', 'SM-G925Z',
    'SM-G9280', 'SM-G9287', 'SM-G9287C', 'SM-G928A', 'SM-G928C', 'SM-G928F',
    'SM-G928G', 'SM-G928i', 'SM-G928K', 'SM-G928L', 'SM-G928N', 'SM-G928N0',
    'SM-G928P', 'SM-G928R4', 'SM-G928S', 'SM-G928T', 'SM-G928V', 'SM-G928W8',
    'SM-G928X', 'SM-G9298', 'SM-G9300', 'SM-G9308', 'SM-G930A', 'SM-G930AZ',
    'SM-G930F', 'SM-G930FD', 'SM-G930K', 'SM-G930L', 'SM-G930P', 'SM-G930R4',
    'SM-G930R6', 'SM-G930R7', 'SM-G930S', 'SM-G930SKL', 'SM-G930T', 'SM-G930T1',
    'SM-G930U', 'SM-G930V', 'SM-G930VC', 'SM-G930VL', 'SM-G930W', 'SM-G930W8',
    'SM-G930X', 'SM-G9350', 'SM-G935A', 'SM-G935AU', 'SM-G935D', 'SM-G935F',
    'SM-G935FD', 'SM-G935J', 'SM-G935K', 'SM-G935L', 'SM-G935P', 'SM-G935R4',
    'SM-G935R6', 'SM-G935R7', 'SM-G935S', 'SM-G935T', 'SM-G935T1', 'SM-G935U',
    'SM-G935V', 'SM-G935VC', 'SM-G935W', 'SM-G935W8', 'SM-G935X', 'SM-G950',
    'SM-G9500', 'SM-G9508', 'SM-G950D', 'SM-G950F', 'SM-G950FD', 'SM-G950J',
    'SM-G950N', 'SM-G950U', 'SM-G950U1', 'SM-G950W', 'SM-G950X', 'SM-G950XC',
    'SM-G950XU', 'SM-G955', 'SM-G9550', 'SM-G9558', 'SM-G955F', 'SM-G955FD',
    'SM-G955J', 'SM-G955N', 'SM-G955U', 'SM-G955U1', 'SM-G955W', 'SM-G955X',
    'SM-G955XU', 'SM-G9600', 'SM-G9608', 'SM-G960F', 'SM-G960FD', 'SM-G960L',
    'SM-G960N', 'SM-G960U', 'SM-G960U1', 'SM-G960US', 'SM-G960UX', 'SM-G960W',
    'SM-G960X', 'SM-G960XU', 'SM-G9650', 'SM-G965F', 'SM-G965FD', 'SM-G965J',
    'SM-G965N', 'SM-G965U', 'SM-G965U1', 'SM-G965UX', 'SM-G965W', 'SM-G965X',
    'SM-G965XU', 'SM-G9700', 'SM-G9708', 'SM-G970F', 'SM-G970FD', 'SM-G970N',
    'SM-G970U', 'SM-G970U1', 'SM-G970W', 'SM-G970X', 'SM-G970XC', 'SM-G970XN',
    'SM-G970XU', 'SM-G9730', 'SM-G9730Z', 'SM-G9738', 'SM-G973C', 'SM-G973D',
    'SM-G973F', 'SM-G973J', 'SM-G973N', 'SM-G973U', 'SM-G973U1', 'SM-G973W',
    'SM-G973XC', 'SM-G973XN', 'SM-G973XU', 'SM-G9750', 'SM-G9758', 'SM-G9758',
    'SM-G975F', 'SM-G975FD', 'SM-G975N', 'SM-G975U', 'SM-G975U1', 'SM-G975W',
    'SM-G975XC', 'SM-G975XN', 'SM-G975XU', 'SM-G977B', 'SM-G977N', 'SM-G977P',
    'SM-G977T', 'SM-G977U', 'SM-G977U1', 'SM-G977W', 'SM-G977XU', 'SM-G97xF',
    'SM-G980A', 'SM-G980F', 'SM-G980F', 'SM-G980F', 'SM-G9810', 'SM-G9810-FIX',
    'SM-G981A', 'SM-G981B', 'SM-G981BR', 'SM-G981C', 'SM-G981N', 'SM-G981N',
    'SM-G981U', 'SM-G981U1', 'SM-G981V', 'SM-G981W', 'SM-G985F', 'SM-G985X',
    'SM-G9860', 'SM-G986B', 'SM-G986N', 'SM-G986U', 'SM-G986U1', 'SM-G986W',
    'SM-G9880', 'SM-G9880-FIX', 'SM-G988B', 'SM-G988BR', 'SM-G988N', 'SM-G988U',
    'SM-G988U1', 'SM-G988W', 'SM-G990B', 'SM-G990B2', 'SM-G990BR', 'SM-G990E',
    'SM-G990U', 'SM-G990U-FIX', 'SM-G990U1', 'SM-G990U2', 'SM-G9910', 'SM-G991B',
    'SM-G991BR', 'SM-G991N', 'SM-G991N', 'SM-G991XU', 'SM-G9960', 'SM-G9968',
    'SM-G996B', 'SM-G996B-FIX', 'SM-G996BR', 'SM-G996N', 'SM-G996X', 'SM-G996XU',
    'SM-G9980', 'SM-G9988', 'SM-G998B', 'SM-G998N', 'SM-G998X', 'SM-G998XU',
    'SM-J730F', 'SM-M017F', )


def get_version(options: Options) -> AndroidVersion:
    filterer = Filterer(versions)

    if options.version_ranges and 'android' in options.version_ranges:
        filterer.version_range(options.version_ranges['android'])

    if options.weighted_versions:
        filterer.weighted_versions(max_range=5)

    choice: AndroidVersion = random.choice(filterer.versions)
    if choice.build_number is not None:
        choice.build_number = choice.build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(random.randint(17, 25), random.randint(0, 12), random.randint(0, 29)))
        choice.build_number = choice.build_number.replace('{v}', '{}'.format(random.randint(1, 255)))
    choice.platform_model = random.choice(platform_models)
    return choice
