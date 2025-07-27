rule auto_rule_20250727022357_9831 {
  strings:
    $o0 = "dword_44B6A4" wide ascii nocase
    $o1 = "_bittestandset" wide ascii nocase
    $o2 = "_mtdeletelocks" wide ascii nocase
  condition:
    3 of ($o*)
}