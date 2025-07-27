rule auto_rule_20250726202757_8383 {
  strings:
    $o0 = "_wincmdln" wide ascii nocase
    $o1 = "dword_15B6DE88" wide ascii nocase
    $o2 = "dword_4141E4" wide ascii nocase
  condition:
    3 of ($o*)
}