rule auto_rule_20250727024027_4958 {
  strings:
    $o0 = "dword_42B890" wide ascii nocase
    $o1 = "x40Fu" wide ascii nocase
    $o2 = "lfFaceName" wide ascii nocase
  condition:
    3 of ($o*)
}