rule auto_rule_20250726140058_1565 {
  strings:
    $o0 = "dword_468074" wide ascii nocase
    $o1 = "bKeyDown" wide ascii nocase
  condition:
    all of them
}