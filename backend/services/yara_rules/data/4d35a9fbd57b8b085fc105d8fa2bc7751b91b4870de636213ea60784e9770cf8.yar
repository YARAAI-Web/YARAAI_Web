rule auto_rule_20250726074151_8031 {
  strings:
    $o0 = "dword_73178" wide ascii nocase
    $o1 = "dword_73190" wide ascii nocase
    $o2 = "dword_72F58" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}