rule auto_rule_20250726204639_2419 {
  strings:
    $o0 = "UScore" wide ascii nocase
    $o1 = "SrcBuf" wide ascii nocase
    $o2 = "Replicator" wide ascii nocase
    $o3 = "j__dosmaperr" wide ascii nocase
  condition:
    4 of ($o*)
}