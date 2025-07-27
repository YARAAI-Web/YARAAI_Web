rule auto_rule_20250727013016_3857 {
  strings:
    $o0 = "dword_10006324" wide ascii nocase
    $o1 = "WSAStartup" wide ascii nocase
    $o2 = "AF8h" wide ascii nocase
  condition:
    3 of ($o*)
}