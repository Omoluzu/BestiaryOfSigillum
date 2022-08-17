from .IGNIS import *
from modules.Aqualin import StartedConfiguration, GamesAqualin

start_game = {
    'aqualin': StartedConfiguration.started_configuration,
    'ignis': IGNIS.start
}

game = {
    'aqualin': GamesAqualin,
    'ignis': IgnisGames,
}
