from .IGNIS import *
from .AZUL import *
from .LCG_ARKHAM_HORROR import *
from modules.Aqualin import StartedConfiguration, GamesAqualin

start_game = {
    'aqualin': StartedConfiguration.started_configuration,
    'ignis': IGNIS.start,
    'azul': AZUL.start,
}

game = {
    'aqualin': GamesAqualin,
    'ignis': IgnisGames,
    'azul': AzulGames,
}
