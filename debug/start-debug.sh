#!/bin/bash

# Dieser Script benötigt Socat. Wird er gestartet öffnet er 2 virtuelle serielle Konsolen
# Die eine konnektiert man mit dARts.py und in die andere kann man Befehle eingeben
# So kann man entwickeln, ohne das Setup zu haben

socat PTY,link=/tmp/virtualcom0,echo=0 PTY,link=/tmp/virtualcom1,echo=0 &
