module AOC where

import Prelude

import Data.Either (Either(..))
import Data.Maybe (Maybe(..))
import Data.String (joinWith, trim)
import Data.String.Utils (lines)
import Effect (Effect)
import Effect.Aff (Aff, effectCanceler, launchAff_, makeAff, nonCanceler)
import Effect.Class (liftEffect)
import Effect.Class.Console (log)
import Effect.Ref as Ref
import Node.Encoding (Encoding(..))
import Node.Process (stdin)
import Node.Stream (onDataString, onEnd, onError, pause)

foreign import stdinIsTTY :: Boolean

getStdin :: Aff (Maybe String)
getStdin =
  makeAff
    $ \res ->
        if stdinIsTTY then do
          res $ Right Nothing
          pure nonCanceler
        else do
          dataRef <- Ref.new ""
          onDataString stdin UTF8 \chunk ->
            Ref.modify_ (_ <> chunk) dataRef
          onEnd stdin do
            allData <- Ref.read dataRef
            res $ Right (Just allData)
          onError stdin $ Left >>> res
          pure $ effectCanceler (pause stdin)

run :: (Array String -> Array String) -> Effect Unit
run f =
  launchAff_ do
    s <- getStdin
    liftEffect $ log
      $ case s of
          Nothing -> "Error reading in input"
          Just s' -> joinWith "\n" $ f (lines $ trim s')
