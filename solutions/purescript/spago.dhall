{-
Welcome to a Spago project!
You can edit this file as you like.
-}
{ name = "my-project"
, dependencies =
  [ "aff"
  , "console"
  , "effect"
  , "node-process"
  , "node-streams"
  , "psci-support"
  , "string-parsers"
  , "strings"
  , "stringutils"
  ]
, packages = ./packages.dhall
, sources = [ "20*/**/*.purs", "helpers.purs" ]
}
