rule auto_rule_20250726165315_6607 {
  strings:
    $o0 = "ZwSetInformationProcess" wide ascii nocase
    $o1 = "dword_77F14" wide ascii nocase
    $o2 = "dword_78228" wide ascii nocase
    $o3 = "dword_7828C" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}