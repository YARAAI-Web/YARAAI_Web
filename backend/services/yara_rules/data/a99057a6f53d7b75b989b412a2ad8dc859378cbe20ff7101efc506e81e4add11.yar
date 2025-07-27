rule auto_rule_20250726215251_9131 {
  strings:
    $o0 = "x3FFFu" wide ascii nocase
    $o1 = "dword_41A028" wide ascii nocase
    $o2 = "_cftof2" wide ascii nocase
  condition:
    3 of ($o*)
}