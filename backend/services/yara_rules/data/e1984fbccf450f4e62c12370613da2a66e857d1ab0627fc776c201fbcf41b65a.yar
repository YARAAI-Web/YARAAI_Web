rule auto_rule_20250726144047_3902 {
  strings:
    $o0 = "bad_array_new_length" wide ascii nocase
    $o1 = "dword_14010F668" wide ascii nocase
    $o2 = "dword_14010F3D0" wide ascii nocase
    $o3 = "dword_14010F2BC" wide ascii nocase
  condition:
    4 of ($o*)
}