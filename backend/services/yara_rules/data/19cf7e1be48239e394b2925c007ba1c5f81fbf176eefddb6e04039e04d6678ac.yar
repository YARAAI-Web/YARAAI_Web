rule auto_rule_20250726084233_6038 {
  strings:
    $o0 = "dword_44A048" wide ascii nocase
    $o1 = "dword_40B004" wide ascii nocase
    $o2 = "dword_449EF8" wide ascii nocase
    $o3 = "byte_44A080" wide ascii nocase
  condition:
    4 of ($o*)
}