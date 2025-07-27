rule auto_rule_20250726114027_6698 {
  strings:
    $o0 = "dword_14000CD0C" wide ascii nocase
  condition:
    all of them
}