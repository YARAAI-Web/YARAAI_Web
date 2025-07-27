rule auto_rule_20250727032043_3127 {
  strings:
    $o0 = "dword_140005668" wide ascii nocase
    $o1 = "xmmword_1400032D0" wide ascii nocase
    $o2 = "xFFFFFFFFFFFFFFDBuLL" wide ascii nocase
    $o3 = "_raise_securityfailure" wide ascii nocase
  condition:
    4 of ($o*)
}