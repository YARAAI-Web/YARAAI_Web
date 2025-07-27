rule auto_rule_20250726123027_5315 {
  strings:
    $o0 = "dword_42FE8A" wide ascii nocase
    $o1 = "x4EC5u" wide ascii nocase
    $o2 = "idAni" wide ascii nocase
  condition:
    3 of ($o*)
}