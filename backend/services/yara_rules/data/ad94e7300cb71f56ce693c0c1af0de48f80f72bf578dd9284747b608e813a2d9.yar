rule auto_rule_20250726130911_2661 {
  strings:
    $o0 = "dword_464290" wide ascii nocase
    $o1 = "__sbh_alloc_block" wide ascii nocase
    $o2 = "stream" wide ascii nocase
  condition:
    3 of ($o*)
}