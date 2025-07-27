rule auto_rule_20250726100815_0269 {
  strings:
    $o0 = "aSoftware" wide ascii nocase
    $o1 = "uiParam" wide ascii nocase
    $o2 = "ucchMax" wide ascii nocase
    $o3 = "ReadConsoleOutputA" wide ascii nocase
  condition:
    4 of ($o*)
}