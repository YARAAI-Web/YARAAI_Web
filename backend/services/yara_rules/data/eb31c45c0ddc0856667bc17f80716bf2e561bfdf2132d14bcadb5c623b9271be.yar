rule auto_rule_20250727010226_4478 {
  strings:
    $o0 = "aMssecsvcExe" wide ascii nocase
    $o1 = "FindResourceA" wide ascii nocase
  condition:
    all of them
}