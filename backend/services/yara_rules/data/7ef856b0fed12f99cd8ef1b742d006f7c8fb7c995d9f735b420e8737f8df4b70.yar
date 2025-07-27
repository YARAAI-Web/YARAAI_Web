rule auto_rule_20250726083255_6248 {
  strings:
    $o0 = "x6D230000209FLL" wide ascii nocase
    $o1 = "stru_42B226" wide ascii nocase
    $o2 = "dword_42A2F6" wide ascii nocase
  condition:
    3 of ($o*)
}