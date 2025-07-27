rule auto_rule_20250726234217_6765 {
  strings:
    $o0 = "SetServiceAsTrustedW" wide ascii nocase
    $o1 = "x51431B00u" wide ascii nocase
    $o2 = "WSACloseEvent" wide ascii nocase
    $o3 = "dword_43B14D" wide ascii nocase
    $o4 = "dword_43B708" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726234220_6277 {
  strings:
    $o0 = "dword_43B0AB" wide ascii nocase
    $o1 = "dword_43B223" wide ascii nocase
    $o2 = "dword_43B6A3" wide ascii nocase
    $o3 = "dword_43B7B7" wide ascii nocase
    $o4 = "dword_43B589" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726234224_2532 {
  condition:
    auto_rule_20250726234217_6765 or auto_rule_20250726234220_6277
}