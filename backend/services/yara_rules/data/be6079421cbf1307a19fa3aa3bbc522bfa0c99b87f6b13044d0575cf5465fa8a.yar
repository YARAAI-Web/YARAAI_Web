rule auto_rule_20250726230601_7711 {
  strings:
    $o0 = "v257" wide ascii nocase
    $o1 = "qword_140556C28" wide ascii nocase
    $o2 = "qword_140556C20" wide ascii nocase
    $o3 = "sha1rnds4" wide ascii nocase
  condition:
    4 of ($o*)
}