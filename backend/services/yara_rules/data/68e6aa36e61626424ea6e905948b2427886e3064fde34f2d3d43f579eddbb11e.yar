rule auto_rule_20250726100228_5940 {
  strings:
    $o0 = "FreeConsole" wide ascii nocase
    $o1 = "GetKeyboardType" wide ascii nocase
  condition:
    all of them
}