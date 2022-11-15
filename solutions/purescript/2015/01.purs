module Year2015.Day01 where

import Prelude

import AOC as AOC
import Control.Alt ((<|>))
import Data.Array (head)
import Data.Either (Either(..))
import Data.Foldable (sum)
import Data.Maybe (Maybe(..))
import Effect (Effect)
import Text.Parsing.StringParser (Parser, runParser)
import Text.Parsing.StringParser.CodePoints (anyChar)
import Text.Parsing.StringParser.CodeUnits (char, string)
import Text.Parsing.StringParser.Combinators (many1)

parser :: String -> Parser Int
parser c = do
  let
      oneIfMatch = string c $> 1
      zeroOW = anyChar $> 0
      convertLettersToList = many1 (oneIfMatch <|> zeroOW)
  list <- convertLettersToList
  pure $ sum list

parse :: String -> String -> Int
parse c s =
  case runParser (parser c) s of
    Left _ -> 0
    Right n -> n

run :: Array String -> Array String
run xs = case head xs of
  Nothing -> ["invalid input"]
  Just s -> [
    show $ (parse "(" s) - (parse ")" s),

  ]

main :: Effect Unit
main = AOC.run run
