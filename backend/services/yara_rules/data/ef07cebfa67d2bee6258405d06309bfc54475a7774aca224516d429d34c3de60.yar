rule auto_rule_20250726124240_6498 {
  strings:
    $o0 = "dword_781C8" wide ascii nocase
    $o1 = "ZwSetInformationProcess" wide ascii nocase
    $o2 = "dword_78144" wide ascii nocase
    $o3 = "dword_781CC" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}