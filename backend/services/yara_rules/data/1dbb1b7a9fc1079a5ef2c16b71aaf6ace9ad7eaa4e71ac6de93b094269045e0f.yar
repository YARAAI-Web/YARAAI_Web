rule auto_rule_20250726090152_5553 {
  strings:
    $o0 = "x2650FA8Fu" wide ascii nocase
    $o1 = "dword_44E41C" wide ascii nocase
  condition:
    all of them
}