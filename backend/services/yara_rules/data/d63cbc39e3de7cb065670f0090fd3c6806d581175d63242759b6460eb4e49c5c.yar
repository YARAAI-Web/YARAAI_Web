rule auto_rule_20250726131318_6703 {
  strings:
    $o0 = "GetWindowModuleFileNameA" wide ascii nocase
    $o1 = "lpszCurrent" wide ascii nocase
  condition:
    all of them
}