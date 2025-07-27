rule auto_rule_20250726130357_4729 {
  strings:
    $o0 = "__sbh_alloc_block" wide ascii nocase
    $o1 = "dword_45CAF4" wide ascii nocase
    $o2 = "_msize" wide ascii nocase
  condition:
    3 of ($o*)
}