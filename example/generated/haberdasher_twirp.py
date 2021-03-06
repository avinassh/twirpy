# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: haberdasher.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient

_sym_db = _symbol_database.Default()

class HaberdasherServer(TwirpServer):

	def __init__(self, *args, service):
		super().__init__(service=service)
		self._prefix = "/twirp/twitch.twirp.example.Haberdasher"
		self._endpoints = {
			"MakeHat": Endpoint(
				service_name="Haberdasher",
				name="MakeHat",
				function=getattr(service, "MakeHat"),
				input=_sym_db.GetSymbol("twitch.twirp.example.Size"),
				output=_sym_db.GetSymbol("twitch.twirp.example.Hat"),
			),
		}

class HaberdasherClient(TwirpClient):

	def MakeHat(self, *args, ctx, request, **kwargs):
		return self._make_request(
			url="/twirp/twitch.twirp.example.Haberdasher/MakeHat",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("twitch.twirp.example.Hat"),
			**kwargs,
		)
