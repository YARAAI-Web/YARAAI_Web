rule auto_rule_20250726221007_6159 {
  strings:
    $o0 = "retf" wide ascii nocase
    $o1 = "uIDEnableItem" wide ascii nocase
    $o2 = "GetStringTypeA" wide ascii nocase
    $o3 = "ReadConsoleOutputA" wide ascii nocase
    $o4 = "lphl" wide ascii nocase
  condition:
    4 of ($o*)
}