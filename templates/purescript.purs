module Year%%YEAR%%.Day%%DAY%% where

import Prelude

import AOC as AOC
import Effect (Effect)
import Node.Stream

run :: Array String -> Array String
run = identity

main :: Effect Unit
main = AOC.run run
