rule auto_rule_20250726192356_4463 {
  strings:
    $o0 = "__sbh_alloc_block" wide ascii nocase
    $o1 = "dword_464670" wide ascii nocase
    $o2 = "dword_465BB4" wide ascii nocase
  condition:
    3 of ($o*)
}