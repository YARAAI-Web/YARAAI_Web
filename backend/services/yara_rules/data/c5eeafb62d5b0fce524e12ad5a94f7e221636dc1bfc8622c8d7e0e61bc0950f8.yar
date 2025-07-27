rule auto_rule_20250726232941_2873 {
  strings:
    $o0 = "aMssecsvrExe" wide ascii nocase
  condition:
    all of them
}