rule auto_rule_20250726223522_2841 {
  strings:
    $o0 = "__sbh_verify_block" wide ascii nocase
    $o1 = "dword_4647CC" wide ascii nocase
    $o2 = "byte_465980" wide ascii nocase
  condition:
    3 of ($o*)
}