rule auto_rule_20250727012208_9882 {
  strings:
    $o0 = "aClassesClsid0e" wide ascii nocase
    $o1 = "FileA" wide ascii nocase
  condition:
    all of them
}