rule auto_rule_20250726104452_4264 {
  strings:
    $o0 = "v236" wide ascii nocase
    $o1 = "dword_140075734" wide ascii nocase
    $o2 = "dword_14007559C" wide ascii nocase
  condition:
    3 of ($o*)
}