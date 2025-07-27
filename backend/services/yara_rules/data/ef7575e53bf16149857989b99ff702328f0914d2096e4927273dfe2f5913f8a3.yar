rule auto_rule_20250726060703_9125 {
  strings:
    $o0 = "dword_100254E4" wide ascii nocase
    $o1 = "dword_100255C0" wide ascii nocase
    $o2 = "dword_10025634" wide ascii nocase
    $o3 = "dword_10025594" wide ascii nocase
  condition:
    4 of ($o*)
}