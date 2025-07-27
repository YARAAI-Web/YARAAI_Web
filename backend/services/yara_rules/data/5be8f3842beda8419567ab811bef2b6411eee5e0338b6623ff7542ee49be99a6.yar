rule auto_rule_20250726090243_6367 {
  strings:
    $o0 = "dword_465074" wide ascii nocase
  condition:
    all of them
}