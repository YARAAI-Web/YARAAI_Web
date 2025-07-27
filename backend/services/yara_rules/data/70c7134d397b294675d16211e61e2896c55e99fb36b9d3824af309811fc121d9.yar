rule auto_rule_20250726154550_4315 {
  strings:
    $o0 = "dword_48D014" wide ascii nocase
    $o1 = "xFF8u" wide ascii nocase
  condition:
    all of them
}