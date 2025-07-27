rule auto_rule_20250727022953_4198 {
  strings:
    $o0 = "GetModuleBaseNameA" wide ascii nocase
    $o1 = "x412B45" wide ascii nocase
    $o2 = "dword_4771A4" wide ascii nocase
    $o3 = "off_476D08" wide ascii nocase
    $o4 = "__from_strstr_to_strchr" wide ascii nocase
  condition:
    4 of ($o*)
}